import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="M5 project",
                 author='Boris',
                 version="1.0.0",
                 long_description=long_description,
                 scripts = ['m5_initial_nn_model.py'],
                 description="Initial NN model for M5 project",
                 packages=setuptools.find_packages(),
                 python_requires='>=3.7',
                 project_urls={
                     "Git url": "https://github.com/borisilin85/M5_project",

                 },
                install_requires = ['pytest']
                 )