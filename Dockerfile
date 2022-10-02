# 
FROM python:3.9

# 
RUN apt-get update

#
RUN apt-get install apt-utils

# 
RUN apt-get install -y ffmpeg libsm6 libxext6 libgl1-mesa-glx

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --upgrade pip

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "7575"]

