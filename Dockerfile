FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive


# Install Redis
RUN apt-get update && \
    apt-get install --no-install-recommends -y redis-server
    
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


COPY ./src/ /app/

EXPOSE 8000

COPY ./start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ./start.sh