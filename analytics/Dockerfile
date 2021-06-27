FROM jupyter:datascience-notebook
RUN mkdir src
WORKDIR /src/
COPY . .
RUN pip install -r requirements.txt
RUN pip install jupyter
ADD notebooks/data_transformation.ipynb /home/jovyan/work/
WORKDIR /home/jovyan/work/


# Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini