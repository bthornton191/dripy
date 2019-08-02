cd rst
sphinx-apidoc -f -o source ..\dripy
call make html
cd ..
robocopy rst\build\html docs /e /mir