if [ "$OSTYPE" == "msys" ]; then
    bc() {
        /c/Users/rd/bin/unix/bc/bin/bc.exe "$@"
    }
fi

# Update version
num1=`cat VERSION`
echo $(echo $num1 + 1 | bc) > VERSION

# Build package
[[ -d build/ ]] && rm -r build/ 
[[ -d dist/ ]] && rm -r dist/
[[ -d nutrical.egg-info/ ]] && rm -r nutrical.egg-info/
python setup.py sdist &&
twine upload --verbose --repository pypi dist/*
