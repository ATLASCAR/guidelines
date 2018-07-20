# Guidelines for LARDEMUA
Contains guidelines and tutorials for developing code for the Laboratory of Automation and Robotics, Department of Mechanical Engineering, University of Aveiro (**LARDEMUA**).

Check the github page [github.com/lardemua](https://github.com/lardemua) or the [lars.mec.ua.pt](http://lars.mec.ua.pt).

![docs/guidelines-readme.png](docs/guidelines-readme.png?raw=true "guidelines")

# Table of Contents

- [Table of Contents](#table-of-contents)
- [The GUI Window](#the-gui-window)
- [Running the system](#running-the-system)
- [Using as an API](#using-as-an-api)
- [Input json format](#input-json-format)
- [Output json format](#output-json-format)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Installation

If this is a python standalone, then just use the pip install and the [requirements.txt file](https://pip.readthedocs.io/en/1.1/requirements.html) mechanism:

```bash
sudo pip install -r requirements.txt
```

## Usage

For the sake of example, lets call this __fantastic__ [python script](scritp/do-nothing.py)

```bash
script/do-nothing.py -n miguel
```

All the arguments are:

```bash
usage: do-nothing.py [-h] -n NAME [-v VALUE]
do-nothing.py: error: argument -n/--name is required
```

## Credits

List the authors, current develpers, inspiring projects, etc.

## License
GNU GP3. See LICENSE for full details.






There are several keys that can be used:

Window Name  | Description
------------- | -------------
**n** or **space** | move to the next frame
**d** | displays the detections for the current frame
**m** | displays the tracker appearance models for the current frame
**s** | displays the distance matrixes for the current frame
**q** | abort and save output json file and crops images (if configured to do so)


