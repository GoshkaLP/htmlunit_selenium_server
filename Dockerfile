FROM openjdk:17-jdk-alpine

WORKDIR /usr/src/selenium

RUN wget -O selenium.jar https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar \
    && wget -O htmlunit.jar https://github.com/SeleniumHQ/htmlunit-driver/releases/download/2.51.0/htmlunit-driver-2.51.0-jar-with-dependencies.jar

EXPOSE 4444

CMD java -cp selenium.jar:htmlunit.jar org.openqa.grid.selenium.GridLauncherV3