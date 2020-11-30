# NMT Attention Alignment Visualizations
An attention alignment visualization tool for command line and web. 

Usage
---------

  - Translate text and get word or subword level alignments using our model code
  - Visualize the alignments
    - in the command line standard output
    - in a web browser (PHP required)

Installation
---------

From the repository - this way you get all files including pregenerated alignments and the web version for viewing.
```bash
git clone https://github.com/TrushaSakharkar/NLP_Project.git
cd NLP_Project
python3 softalignments/process_alignments.py -i input/alignments.txt -o color/web
```

From the zip - this way you get all files including pregenerated alignments and the web version for viewing.
```bash
unzip filename.zip
cd NLP_Project
python3 softalignments/process_alignments.py -i input/alignments.txt -o color/web
```

Requirements
---------

* Python 3.6 or newer

    * NLTK for BLEU calculation(requires Python versions 3.5, 3.6, 3.7, or 3.8)
	
	* Numpy
	
	```bash
	pip3 install numpy nltk
	```

* PHP 5.4 or newer (for web visualization)

Examples
---------

  - in the command line as shaded blocks. 
	```sh
	python3 softalignments/process_alignments.py -i input/alignments.txt -o color
	```
	
	  or
	```sh
	python3 softalignments/process_alignments.py -i input/alignments.txt -o block2
	```
		
  - in the browser as links between words
	
	```sh
	python3 softalignments/process_alignments.py -i input/alignments.txt -o web
	```

<!-- Screenshots
---------
Color, Block, Block2  
![N|Solid](https://github.com/M4t1ss/sAliViz/blob/master/assets/Screenshots/colorAlignments.PNG?raw=true) ![N|Solid](https://github.com/M4t1ss/sAliViz/blob/master/assets/Screenshots/blockAlignments.PNG?raw=true) ![N|Solid](https://github.com/M4t1ss/sAliViz/blob/master/assets/Screenshots/block2.png?raw=true) 

Web
![N|Solid](https://github.com/M4t1ss/sAliViz/blob/master/assets/Screenshots/webAlignments.PNG?raw=true)

Compare
![N|Solid](https://github.com/M4t1ss/sAliViz/blob/master/assets/Screenshots/webCompare.png?raw=true)
 -->