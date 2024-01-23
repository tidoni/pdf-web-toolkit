FROM python:3.11-slim
# FROM python:3.11.3

# set the working directory
WORKDIR /app
RUN mkdir /app/uploads
RUN mkdir /app/split
RUN mkdir /app/merge
RUN mkdir /app/projects
RUN apt-get update

# install dependencies
COPY ./requirements.txt /app
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

CMD ["bash", "init.sh"]
