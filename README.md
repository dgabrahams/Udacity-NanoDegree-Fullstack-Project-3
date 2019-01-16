# Udacity Fullstack Nano Degree - Project 3

### Overview
---

The instructions in this readme will get a copy of the project up and running on a local machine for development and testing purposes.

### Prerequisites
---

It is assumed that an active connection to the internet will be available at all times. To run this application on a local environment, Git, Vagrant and Virtualbox are required, plus access to Terminal (MAC Linux) or Command Prompt (Windows).

### MAC AND WINDOWS

To determine whether you have Python installed, open the Terminal application, type the following, and press Return:
```
vagrant --version
```

This command will report the version:
```
Vagrant 2.1.5
```

If your machine does not recognise the command, then you might need to install it.
```
https://www.vagrantup.com/intro/getting-started/install.html
```

To determine whether you have Virtualbox installed, open the Terminal application, type the following, and press Return:
```
vboxmanage --version
```

This command will report the version:
```
5.2.22r126460
```

If your machine does not recognise the command, then you might need to install it.
```
https://www.virtualbox.org/manual/ch02.html
```

To determine whether you have GIT installed, open the Terminal application, type the following, and press Return:
```
git --version
```

This command will report the version:
```
git version 2.18.0
```

If your machine does not recognise the command, then you might need to install it.
```
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
```

### INSTALL AND RUN
---

To install the application, assuming that the required prerequisite software is installed, use GIT to clone the repository using a terminal console.

Clone: https://github.com/dgabrahams/Udacity-NanoDegree-Fullstack-Project-3.git

To clone run:
```
git clone https://github.com/dgabrahams/Udacity-NanoDegree-Fullstack-Project-3.git
```

It should build into your current working folder, and produce an output similar to that found below:
```
Database
```

Note where this folder is for later use.

In another folder outside of the item above, download or clone the Virtual Machine:
```
git clone https://github.com/udacity/fullstack-nanodegree-vm
```

Navigate into the newly created folder and then into the 'vagrant' subfolder:
```
cd fullstack-nanodegree-vm/vagrant
```

Into the vagrant folder, download/copy from the project database folder or clone (ensure to clone elswhere and copy over) the database:
```
git clone https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
```

From the project folder, copy over the following files into the VM machine vagrant folder:
```
newsdata.sql
project3-reporting-tool.py
```

Open the terminal navigating to the vagrant folder and perform the following actions:
```
vagrant up
```

It could take some time to build.

When ready, ssh into the machine:
```
vagrant shh
```

Navigate to the shared folder:
```
cd /vagrant
```

Run the script for this project:
```
python project3-reporting-tool.py
```

### License
---

This project is licensed under the MIT License.

### Acknowledgments
---
