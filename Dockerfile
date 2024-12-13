FROM python 
# using python image from docker hub 
WORKDIR /ashucode 
# creating and changing folder in docker image
COPY demo.py /CLOUD_TESTING/
CMD [ "python" , "demo.py" ]
# run the python code while creating container