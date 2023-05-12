# VALIDADOR DO XML DO SISTEMA GISS JUNDIAI

Este validador é um esforço experimental para validar os arquivos do novo XML

***USE POR SUA CONTA E RISCO!!***

Até o momento não havia arquivo XSD disponivel

O XSD utilizado aqui é baseado na versão da ABRASF e ajustado para o GISS

O trabalho foi feito baseado no arquivo **arquivo 2.4 correto jundai_08-05.xml** fornecido pela equipe da Prefeitura

## Como instalar o python

Se você usa Linux, eu não preciso explicar ;)

Se você usa Windows, faça o download do instaldor em https://www.python.org/downloads/, execute e faça next...next...finish

## Como usar o validador

1. Instale o python3
2. Ajuste o seu XML trocando a primeira linha
3. Subtitua no arquivo validador-xml.py o nome do seu xml
4. execute python3 validador-xml.py

Se tudo foi bem você deve receber a mensagem abaixo:

```
The XML file is valid according to the XSD schema, ignoring specific errors.
```

Ele valida o arquivo **arquivo 2.4 correto jundai_08-05-modificado.xml**

## Outras dicas

### MELD: comparador de arquivos

Para ajustar o XML eu utilizei o program **meld** para comparar o arquivo exemplo (arquivo 2.4 correto jundai_08-05.xml)
com o meu.

No Ubuntu vem nos pacotes: **sudo apt install meld**

Em outras distros e Windows é preciso procurar na Internet