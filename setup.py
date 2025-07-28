from setuptools import setup

try:
    from pypandoc import convert

    long_desc = convert(open("README.md").read(), to="rst", format="markdown")
except:
    long_desc = (
        "pymdknit - Elegant, flexible and fast dynamic report generation with python"
    )

setup(
    name="pymdknit",
    version="0.1.1",
    description="Elegant, flexible and fast dynamic report generation with python",
    long_description=long_desc,
    author="Jan Schulz",
    author_email="jasc@gmx.net",
    maintainer="Adam Twardoch",
    maintainer_email="adam+github@twardoch.com",
    url="https://github.com/janschulz/pymdknit/issues",
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Utilities",
    ],
    packages=["pymdknit"],
    entry_points={
        "console_scripts": ["pymdknit = pymdknit.pymdknitapp:launch_new_instance"]
    },
    install_requires=[
        "pyyaml",
    ],
)
