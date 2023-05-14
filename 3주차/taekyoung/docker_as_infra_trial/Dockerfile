FROM python:3.10

LABEL title="python sample application"
LABEL writer="taekyoung.lee"

RUN apt-get update && apt-get -y install    neovim  \
                                            curl    \
                                            wget

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /proj

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
