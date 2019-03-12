pip freeze > requirements.txt
rmdir /S /Q dist
rmdir /S /Q build
rmdir /S /Q dripy.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*