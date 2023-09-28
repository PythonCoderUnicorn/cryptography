#Steganography

`steghide`
regular_image.jpeg

create a text file `super_secret_stuff.txt`
<span style="color:#0fff3f">`echo "This is super secret text!" > ./super_secret_stuff.txt`</span>

## embedding data

embed .txt into the image

<span style="color:#0fff3f">`steghide embed -cf regular_image.jpg -ef super_secret_stuff.txt`</span>
passphrase: secret"

- `cf` cover file name to embed data
- `ef` embed file

## extract data from image

- need to know passphrase
- make sure the `super_secret_stuff.txt` is in another directory

<span style="color:#0fff3f">`steghide extract -sf heman-sec.jpeg`</span>
enter passphrase


----

- image `rubiks.jpg`
- `file rubiks.jpg` shows its JSON data
- `solitaire.exe` = JSON
- `xxd computer.jpg`  on GitHub it was an image
- `strings computer.jpg` 
- `binwalk computer.jpg` 



---
### Resources 

- [Python: LSB-Steg](https://github.com/RobinDavid/LSB-Steganography)
- [Python: Steganography](https://github.com/ragibson/Steganography)
- [stego-toolkit](https://github.com/DominicBreuker/stego-toolkit)
- [StegOnline](https://github.com/Ge0rg3/StegOnline)
- 


---

## YouTube

- [Black Hat: Advanced JPEG Steganography and Detection by John Ortiz](https://www.youtube.com/watch?v=BQPkRlbVFEs)
- [Computerphile - Secrets Hidden in Images (Steganography)](https://youtu.be/TWEXCYQKyDc)
- [Computerphile - Colourspaces (JPEG Pt 0)](https://www.youtube.com/watch?v=LFXN9PiOGtY)
- [Computerphile - JPEG 'files' & Colour (JPEG Pt 1)](https://www.youtube.com/watch?v=n_uNPbdenRs)
- [Computerphile - JPEG DCT, Discrete Cosine Transform (JPEG Pt 2)](https://www.youtube.com/watch?v=Q2aEzeMDHMA)
- [Computerphile - the problem with JPEG](https://www.youtube.com/watch?v=yBX8GFqt6GA)
- [Cryptography for Everybody - How to Hide Secret data in Text (Part 1)](https://www.youtube.com/watch?v=opOEZCezzkY)
- [Reducible - The Unreasonable Effectiveness of JPEG: A signal processing approach](https://www.youtube.com/watch?v=0me3guauqOU)
- 


---
- https://github.com/c1ph0r/stego
- https://github.com/c1ph0r/bbv2cards/tree/main

Stegananalysis Steps
1. look at image
2. `$ strings`
3. `$ exiftool`
4. `$ binwalk`
5. `$ stegsolve`
6. `$ D.I.T.T` [digital invisible ink toolkit (Java) ](https://github.com/drkatnz/diit)

file: `1r2g3b.png` 
tool: `https://stegonline.georgeom.net/upload`
upload image > extract files > select R 1 G 2 B 3 > get flag


Python hide info inside a JPEG
- https://www.youtube.com/watch?v=r-7d3w5xerY























