import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tunnel",
    version="0.0.2",
    author="Brett Beeson",
    author_email="brettbeeson@fastmail.com",
    include_package_data=True,
    description="SSH Tunnel Utilties",
    long_description="Client makes ssh port to server at unknown port, server writes ssh config to get back to client",
    # long_description_content_type="text/markdown",
    url="https://github.com/brettbeeson/tunnel",
    packages=setuptools.find_packages(),
    scripts = ['tunnel.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    # todo: change from boto to minio. boto is massive
    install_requires=['psutil', 'sshconf'
    ],
    python_requires='>=3.6',
)
