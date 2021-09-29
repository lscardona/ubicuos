FROM node:12.22.1-alpine3.11
#declaración de imagen
WORKDIR /app
#declaración de directorio de trabajo
COPY . .
#copiado de toda la información
RUN yarn install --production
#ejecución de un comando
CMD ["node", "/app/publicacion.js"]
#punto de entrada de la imagen