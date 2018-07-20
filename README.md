# Description
Contains guidelines and tutorials for developing code for the Laboratory of Automation and Robotics at hte Department of Mechanical Engineering, University of Aveiro (lars.mec.ua.pt).

# Table of Contents

- [Table of Contents](#table-of-contents)
- [The GUI Window](#the-gui-window)
- [Running the system](#running-the-system)
- [Using as an API](#using-as-an-api)
- [Input json format](#input-json-format)
- [Output json format](#output-json-format)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Installation

## Usage

## Where to get help

* Documentation
* Mailing List
* Wiki

## Contribution Guidelines
Tell me how I can help out including wanted features and code standards

## Contributor List
List the humans behind the project

## Credits, Inspiration, Alternatives
Tell me if this is a fork of or otherwise inspired by another project.

## License
X license. See LICENSE for full details.

# The GUI Window

The gui window display a lot of information about the detections and trackers of the current scene.

![docs/scene.png](docs/scene.png?raw=true "scene")

There are several keys that can be used:

Window Name  | Description
------------- | -------------
**n** or **space** | move to the next frame
**d** | displays the detections for the current frame
**m** | displays the tracker appearance models for the current frame
**s** | displays the distance matrixes for the current frame
**q** | abort and save output json file and crops images (if configured to do so)

Here are examples of detections and tracker models for the scene above:

![docs/trackers_and_detections.png](docs/trackers_and_detections.png?raw=true "trackers_and_detections")

And some examples of distance matrixes:

![docs/distance_matrixes.png](docs/distance_matrixes.png?raw=true "distance_matrixes")

# Running the system

From the vintra_tracking directory, run:

```bash
test/gui.py -p ../../datasets/Tracking/5fps/Main_ave_clip/frames/ -d ../../datasets/Tracking/5fps/Main_ave_clip/input.json -g -n 5 -ns 30 -b 0.02 -f 0.15 -da 0.5 -wa 0.5 -m 0.2 -s
```

This contains the parameters used in our last fine tunning session.

You can also set the values of several parameters. See the instructions bellow.

```bash
usage: gui.py [-h] -p PATH_TO_IMAGES -d DETECTIONS_FILE [-a USE_APPEARANCE]
              [-n N_FRAMES_TO_LOOSE_TRACK]
              [-ns N_FRAMES_TO_LOOSE_TRACK_FOR_STOPPED]
              [-m MAXIMUM_DISTANCE_FOR_ASSOCIATION] [-f FLICKERING_THRESHOLD]
              [-o OUTPUT_FILE] [-g] [-s] [-c SAVE_CROPS] [-b BORDER_SIZE]
              [-da DISTANCE_TO_COMPUTE_APPEARANCE]
              [-wa WINDOW_SIZE_TO_COMPUTE_APPEARANCE]
              [-ss STD_TO_CONSIDER_STOPPED]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH_TO_IMAGES, --path_to_images PATH_TO_IMAGES
                        path to the folder that contains the images
  -d DETECTIONS_FILE, --detections_file DETECTIONS_FILE
                        file containing the detections per image
  -a USE_APPEARANCE, --use_appearance USE_APPEARANCE
                        use appearance based tracking. More accurate but
                        slower.
  -n N_FRAMES_TO_LOOSE_TRACK, --n_frames_to_loose_track N_FRAMES_TO_LOOSE_TRACK
                        number of frames to maintain the tracker without an
                        associated detection before deleting it. This is
                        applied to moving objects or to those which still have
                        an undefined state.
  -ns N_FRAMES_TO_LOOSE_TRACK_FOR_STOPPED, --n_frames_to_loose_track_for_stopped N_FRAMES_TO_LOOSE_TRACK_FOR_STOPPED
                        number of frames to maintain the tracker without an
                        associated detection before deleting it. This is
                        applied only to static objects.
  -m MAXIMUM_DISTANCE_FOR_ASSOCIATION, --maximum_distance_for_association MAXIMUM_DISTANCE_FOR_ASSOCIATION
                        maximum allowed distance to consider an association.
                        Distance must be bellow this value to be considered an
                        association. This parameter must be retunned whenever
                        the appearance based distance formula is changed.
  -f FLICKERING_THRESHOLD, --flickering_threshold FLICKERING_THRESHOLD
                        threshold under which all motions are considered zero.
                        Useful to zero the residual motion of parked cars. As
                        a ratio of the (W+H) size of the detection
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        path to the output file
  -g, --show_gui        show the graphical user interface
  -s, --show_distance_matrixes
                        shows the distance matrixes
  -c SAVE_CROPS, --save_crops SAVE_CROPS
                        save track crops in a give path
  -b BORDER_SIZE, --border_size BORDER_SIZE
                        Forbidden image canvas as a percentage of the image
                        height
  -da DISTANCE_TO_COMPUTE_APPEARANCE, --distance_to_compute_appearance DISTANCE_TO_COMPUTE_APPEARANCE
                        Maximum distance threshold between the detection and
                        the tracker window centers in order to compute the
                        appearance based distance. As a function of the
                        tracker window diagonal
  -wa WINDOW_SIZE_TO_COMPUTE_APPEARANCE, --window_size_to_compute_appearance WINDOW_SIZE_TO_COMPUTE_APPEARANCE
                        Maximum distance threshold between the sizes of the
                        detection and the tracker windows in order to compute
                        the appearance based distance. As a percentual
                        variation over the tracker window size
  -ss STD_TO_CONSIDER_STOPPED, --std_to_consider_stopped STD_TO_CONSIDER_STOPPED
                        max standard deviation to consider the object as
                        stopped
```

# Using as an API

You can also use the vintra_tracking class in your own code. Here is the docstring for the initialization:

```python
def __init__(self, path_to_images, detections_file, use_appearance = False, n_frames_to_loose_track = 85, maximum_distance_for_association = 150, flickering_threshold = 80, output_file=None):
"""Implements the multi target tracking of vehicles and pedestrians

  Args: 
    use_appearance (bool): use appearance based tracking. More accurate but slower.
    n_frames_to_loose_track (int): number of frames to maintain the tracker without an associated detection before deleting it
    maximum_distance_for_association (float): maximum allowed distance to consider an association. Distance must be bellow this         value to be considered an association. This parameter must be retunned whenever the distance formula is changed, i.e.,         when using appearance or not
    flickering_threshold (float): threshold under which all motions are considered zero. Useful to zero the residual motion of         parked cars.
    output_file (str): If an output_file is defined it will save results to a json file instead of returning the list of tracks
    
    Returns:
      The output is given as a json file when calling the writeTrackersToFile method, so there are no return parameters. 

""" 
```

After initialization you just call the update function. See the [gui.py](https://github.com/miguelriemoliveira/vintra-miguel/blob/master/vintra_tracking/test/gui.py) for an example.

# Input json format

```json
{"0000001.jpg": {"width": 640, "frame": 1, "detections": [{"center": [0.269, 0.35], "_id": "58b6ebb1cddef36be7dd3213", "type": "cars", "score": 0.267, "bbox": {"y": 0.306, "x": 0.227, "w": 0.07, "h": 0.071}}, {"_id": "58b6ebb1cddef36be7dd3215", "type": "cars", "score": 0.162, "bbox": {"y": 0.344, "x": 0.163, "w": 0.076, "h": 0.068}}, {"_id": "58b6ebb1cddef36be7dd3217", "type": "cars", "score": 0.28, "bbox": {"y": 0.358, "x": 0.113, "w": 0.076, "h": 0.074}}, {"_id": "58b6ebb1cddef36be7dd3219", "type": "cars", "score": 0.372, "bbox": {"y": 0.383, "x": 0.014, "w": 0.105, "h": 0.096}}, {"_id": "58b6ebb1cddef36be7dd321b", "type": "pedestrians", "score": 0.169, "bbox": {"y": 0.233, "x": 0.316, "w": 0.024, "h": 0.101}}], "height": 360}
```

