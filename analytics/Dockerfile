FROM jupyter:datascience-notebook
RUN mkdir src
WORKDIR /src/
COPY . .
RUN pip install -r requirements.txt
RUN pip install jupyter
ADD notebooks /home/jovyan/work
WORKDIR /home/jovyan/work/data_transformation.ipynb


# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

CMD jupyter notebook /home/jovyan/work/data_transformation.ipynb