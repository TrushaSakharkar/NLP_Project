# coding: utf-8
import io, unicodedata, re, sys, getopt, string, os, webbrowser, math, ntpath, numpy as np
import tempfile, shutil
from time import gmtime, strftime
from imp import reload
try:
    from softalignments.functions import *
except ImportError:
    sys.path.insert(1, 'softalignments')
    from functions import *
try:
    import configparser as cp
except ImportError:
    import ConfigParser as cp

def main():
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hi:o:s:t:f:n:a:b:c:d:g:r:v:w:x:y:")
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit()
        elif opt == '-i':
            inputfile = arg
        elif opt == '-o':
            outputType = arg
   
    try:
        de_bpe
    except NameError:
        de_bpe = False
    
    try:
        referencefile
    except NameError:
        referencefile = False
    try:
        inputfile
    except NameError:
        print ('Provide an input file!\n')
        printHelp()
        sys.exit()
   
    try:
        num
    except NameError:
        num = -1
    try:
        outputType
    except NameError:
        outputType = 'web'
    (srcs, tgts, alis) = readNematus(inputfile, de_bpe)
    
    data = list(zip(srcs, tgts, alis))
    
    foldername = ntpath.basename(inputfile).replace(".","") + "_" + strftime("%d%m_%H%M", gmtime())
    if outputType == 'web':
        folder = './web/data/' + foldername
    else:
        folder = tempfile.mkdtemp()

    try:
        os.stat(folder)
    except:
        os.mkdir(folder)
        
    if(referencefile):
        shutil.copyfile(referencefile, folder + "/" + ntpath.basename(inputfile) + '.ref.txt')
        refs = readSnts(referencefile)
    else:
        refs = False
    
    processAlignments(data, folder, inputfile, outputType, num, refs)
            
    if outputType == 'web':
        webbrowser.open("http://127.0.0.1:47155/?directory=" + foldername)
        os.system("php -S 127.0.0.1:47155 -t web")
    else:
        os.remove(folder + "/" + ntpath.basename(inputfile) + '.ali.js')
        os.remove(folder + "/" + ntpath.basename(inputfile) + '.src.js')
        os.remove(folder + "/" + ntpath.basename(inputfile) + '.trg.js')
        os.remove(folder + "/" + ntpath.basename(inputfile) + '.con.js')
        os.remove(folder + "/" + ntpath.basename(inputfile) + '.sc.js')
        shutil.rmtree(folder)

if __name__ == "__main__":
    if sys.version[0] == '2':
        reload(sys)
        sys.setdefaultencoding('utf-8')
    main()
