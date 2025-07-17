# RCDS-parallel-programming-in-python

## Webinar Instructions

To complete this course, you will need to attend the Microsoft Teams session. You should do this using the Microsoft Teams app, signed into your Imperial account, if you have one. You should have a working microphone and camera. 

## Face to Face Course Instructions

This course will take place in an ICT computer room and so laptops are not required but you may bring one if you wish.

## Self-Study

This course can be studied independently at your own pace. Make sure you have completed the pre-course instructions described above. Once your GitHub account is set up and registered with GitHub Education, open a Codespace as described below. You can then work your way through the jupyter notebooks in the the order they are numbered. Make sure to experiment with the tools and complete the exercises to gain experience of using the tools yourself.

## Accessing Course Materials

The course materials are stored in this Github repository. You may review them before the course if you want to, but you don't have to.

During the course you will need to be able toview the course materials and run the codes in the repository. The easiest way to run the course materials in a GitHub Codespace (instructions below), which can be done on a computer room computer for a face to face session, or your own laptop. This requires no setup in advance past the pre-course instructions above. 

Alternatively, you may download the course materials on to your own computer, install [Visual Studio Code](https://code.visualstudio.com/) and install the following extensions within VS Code:
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

You will also need to [donwload a version of MPICH](https://www.mpich.org/downloads/) suitable for your operating system. You will also need to install the following Python packages:

* ipykernel
* numpy
* matplotlib
* mpi4py
* pandas

These packages are specified in the `requirements.txt` file which you could use to install the packages if you're familiar with how to use this kind of file.

## Opening a Codespace

This course is designed to run inside of a [Codespace](https://docs.github.com/en/codespaces/overview). A Codespace is a development environment hosted by GitHub directly from a repository. To use this, you can click [this link](https://codespaces.new/ImperialCollegeLondon/RCDS-parallel-programming-in-python?quickstart=1). Click `Change options' and change the `Machine Type` to 4-core, then click "Create new codespace". This will create a Codespace of your own. This will take a minute or so to initialise. You may be asked to reload the page. If so, do reload the page. If the Codespace seems to get stuck loading, reloading the page can often fix the problem.

Once your Codespace has initialised, it will remain associated with your GitHub account for around a month, when it will expire. Your Codespace will be given a name like "fuzzy-barnacle" so you can identify it. To reopen it on a future occasion, either visit [this page](https://codespaces.new/ImperialCollegeLondon/RCDS-parallel-programming-in-python?quickstart=1) again and click `Resume this Codescpae`, or click the green `Code` button on the main repository page, then select the Codespace, click ```Open```, then ```Open in Browser```.

## Downloading Course Materials

To download the content of the files within the Codespace, open the Files tab on the left, select the files, right click and click ```Download``` button. Alternatively, if you're familiar with GitHub, you can open the source control tab on the left, you can commit and push changes. This will fork the repository with your changes. Either of these options will allow you to keep a copy of the course notes with your solutions to the exercises, etc.

## Post-Course Follow-Up: ReCoDE Exemplar
The RCDS team has curated a collection of annotated [exemplar projects](https://imperialcollegelondon.github.io/ReCoDE-home/exemplars/) known as [ReCoDE](https://imperialcollegelondon.github.io/ReCoDE-home/) which demonstrate core research computing and data science principles applied to real problems. Each exemplar is a real project created by an Imperial student based on their research. Each exemplar is accompanied by detailed descriptions of how they work, and the design decisions taken when constructing the code. There are two Fortran exemplars:

* [**Modelling Organic Crystals Using a Lattice Hamiltonian**](https://imperialcollegelondon.github.io/ReCoDE_Lattice_Hamiltonian/) This exemplar creates a simplified model of an organic crystal, calculating the system's excited states under illumination. It includes an [example](https://imperialcollegelondon.github.io/ReCoDE_Lattice_Hamiltonian/07-Using-multiprocessing/) of using `multiprocessing` to parallelise for-loops.
* [**Mandlebrot Set**](https://imperialcollegelondon.github.io/ReCoDE-Exploration-Mandelbrot-Set/) This exemplar is written in C++ demosntrates how to create and display the Mandlebrot set. It includes a [discussion](https://imperialcollegelondon.github.io/ReCoDE-Exploration-Mandelbrot-Set/Multithreading%20Techniques/Parallel%20version%20using%20MPI/) of the architecture of paralel code using MPI. Although the code is written in C++, many of the MPI practices translate well into Python.
* [**Euler-Maruyama method**](https://imperialcollegelondon.github.io/ReCoDe-Euler-Maruyama/) This exemplar demosntrates how sovle stochastic differential equations in Python, including a [parallel implementation](https://imperialcollegelondon.github.io/ReCoDe-Euler-Maruyama/5-Parallel-Euler-Maruyama-Class/) using joblib.

