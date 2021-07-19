# Color Transfer between Images

This repository is for Color transfer between images introduced in the following paper

E. Reinhard, M. Adhikhmin, B. Gooch and P. Shirley, "Color transfer between images", IEEE Computer Graphics and Applications 2001, [[link]](https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf)


## Introduction
They use a simple statistical analysis to impose one image's color characteristics on another. They can achieve color correction by choosing an appropriate source image and apply its characteristic to another image.

## Test
- requirement package
```
$ virtualenv venv
$ source ./venv/bin/active
(venv)$ pip install opencv-python
(venv)$ pip install numpy
```
- start
```
(venv)$ python main.py
```

## Result

- input

![](https://i.imgur.com/0nn0EeJ.jpg)

- target

![](https://i.imgur.com/F5KvO6X.jpg)

- result

![](https://i.imgur.com/dR6ePxL.jpg)




(image source: [WIDER_val_image](http://shuoyang1213.me/WIDERFACE/))
## Citation

If you find the code helpful in your resarch or work, please cite the following papers.

```
@ARTICLE{946629,
  author={Reinhard, E. and Adhikhmin, M. and Gooch, B. and Shirley, P.},
  journal={IEEE Computer Graphics and Applications}, 
  title={Color transfer between images}, 
  year={2001},
  volume={21},
  number={5},
  pages={34-41},
  doi={10.1109/38.946629}}
```
