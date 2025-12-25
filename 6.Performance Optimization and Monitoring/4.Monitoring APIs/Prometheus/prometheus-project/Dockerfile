#which python version to use
FROM python:3.10

#setting working directory 
WORKDIR /app

#copying application files to the container
COPY ./app /app

#installing required packages
#Can be replaced with a requirements.txt file for larger projects
RUN pip install fastapi uvicorn prometheus-fastapi-instrumentator

#command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]