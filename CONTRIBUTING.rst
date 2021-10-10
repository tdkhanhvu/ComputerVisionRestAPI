.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given. The chosen workflow strategy is Github Flow.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/tdkhanhvu/ComputerVisionRestAPI/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

ComputerVisionRestAPI could always use more documentation, whether as part of the
official ComputerVisionRestAPI docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/tdkhanhvu/ComputerVisionRestAPI/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `ComputerVisionRestAPI` for local development.

1. Fork the `ComputerVisionRestAPI` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:tdkhanhvu/ComputerVisionRestAPI.git

3. Use conda to install the dependency for the Server side:

   .. code-block:: console

       $ conda env create -f ComputerVisionServer.yml

   Use conda to install the dependency for the Client side:

   .. code-block:: console

       $ conda env create -f ComputerVisionClient.yml
	   
   Aternatively, you can download a Docker image using the below command:
   
   .. code-block:: console

       $ docker pull tdkhanhvu/cv-face-recognition

4. Create a branch for local development and make your changes locally::

    $ git checkout -b name-of-your-bugfix-or-feature

5. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.
   For example, if the package uses the poetry package management library, black formatting style and pytest for testing::

    $ poetry run black ComputerVisionRestAPI
    $ poetry run pytest

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

Code of Conduct
---------------
Please note that the ComputerVisionRestAPI project is released with a Contributor Code of Conduct. By contributing to this project you agree to abide by its terms.
