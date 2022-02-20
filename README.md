#### unittest module/library is part of python installation
#### pytest is external/third_party library. Explicitly need to install as part of requirements file.

pytest has built on top of unittest module.

Pytest has rich inbuilt features which require less piece of code compared to unittest. 

Unittest has **setUp** and **tearDown** methods which can be called before after every tests. Same can be achieved using **pytest fixtures**. 

In the case of unittest, we have to import a module, create a class and then define testing functions inside the class. But in the case of pytest, we have to define the functions and assert the conditions inside them