FROM python:3.8-slim AS server

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements.txt /server/
RUN pip install -r requirements.txt

COPY ./server /server

RUN python ./manage.py collectstatic --noinput

#########################################

FROM nginx:1.19.5

RUN rm -v /etc/nginx/nginx.conf
COPY ./nginx/nginx.conf /etc/nginx/

RUN mkdir /nginx
COPY --from=server /server/staticfiles /nginx/static
