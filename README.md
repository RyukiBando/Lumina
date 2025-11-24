- README em [PT-BR](#PT-BR)
#### PT-BR
# Lumina
Um Upscaler usando IA SRCNN com implementação do Pytorch
## O que é?
Nossa implementação e completamente baseada no [**Papel original**](https://arxiv.org/abs/1501.00092v3) de SRCNN com pequenas mudanças utilizando métodos mais modernos.

- CNN e uma rede neural de convulações onde cada camada analisa, mapeia e refina a imagem e melhora sua nitidez
    * O Modelo utiliza três camadas neurais, onde cada camada tem sua função na contrução da imagem em maior resolução, explicação fornecida no codigo, cada camada possui um Kernel que interpreta a imagem em areas de tamanho "X", nosso modelo tem kernel de tamanho: **9-1-5** respectivamente
## Como e Treinada?
O modelo e alimentado somente as imagem de alta resolução dentro de uma pasta e automaticamente faz a diminuição artificial de resolução internamente, utiliza filtro GAUSSIAN para borrar a imagem e a recorta em pedaços para melhora do aprendizado\
<sub> *Outros métodos e valores são discutidos no proprio codigo, qualquer duvida utilizar discussão* </sub>

## Como rodar localmente?
Simples, baixe o arquivo modelo.py e coloque dentro de uma pasta, jubto com o aruivo modelo.py crie outra pasta chamada Database(ou qualquer nome de preferencia) e coloque a pasta contendo as imagens de alta resolução para teste.
### Criando primeiro modelo
- linha 22: `continuar` mude para **False**
- linha 23: `image_dir` mude o caminho para caminho feito
- linha 32: `epochs` Loops feitos, comece com valores baixos para teste (Ex. 1000)
- linha 33: `scale` mude para **2** ou valor de escala desejada
- linha 41-42: Troque `f"Set14 scale:{scale}"` para o nome da sua pasta contendo a imagem
### Continuar o treino por onde parou
- linha 22: `continuar` mude para **True**
> [!CAUTION]
> Verifique se o caminho na linha 41-42 esta correto

## Resultado
#### Set5
*Modelo*  | *Escala* | *Bicúbico* | *SRCNN* | *SSIM*
:---  | :---: | :---: | :---: |  :---: |
**Original** | 3x | 30.39dB | 32.75dB | 0.9090
**SRCNN-Pytorch** | 3x | 30.38dB | 32.39dB | 0.9090
#### Set14
*Modelo* | *Escala* | *Bicúbico* | *SRCNN* | *SSIM*
:--- | :---: | :---: | :---: |  :---: |
**Original** | 3x | 30.39dB | 32.75dB | 0.9090
**SRCNN-Pytorch** | 3x | 30.38dB | 32.39dB | 0.9090

### Exemplos
* **Ground Truth** e imagem original de alta resolução, para comparação
* **Bicúbico** metodo usado para baixa a resolução da imagem, imagem usada para recriar a de alta resolução na IA
* **SRCNN** Utilizando o modelo SRCNN para aumentar a imagem Bicúbica

|           Ground Truth           |               Bicúbico x3               |               SRCNN x3               |
| :------------------------------: | :------------------------------------: | :----------------------------------: |
| ![](./Examples/butterfly_GT.png) | ![](Examples/butterfly_bicubic_x3.png) | ![](Examples/butterfly_srcnn_x3.png) |
|                                  |    <sub>PSNR 32.75dB SSIM 0.9890</sub> |  <sub>PSNR 32.75dB SSIM 0.9890</sub> |
|    ![](Examples/head_GT.png)     |   ![](Examples/head_bicubic_x3.png)    |   ![](Examples/head_srcnn_x3.png)    |
|                                  |    <sub>PSNR 32.75dB SSIM 0.9890</sub> |  <sub>PSNR 32.75dB SSIM 0.9890</sub> |
|    ![](Examples/woman_GT.png)    |   ![](Examples/woman_bicubic_x3.png)   |   ![](Examples/woman_srcnn_x3.png)   |
|                                  |    <sub>PSNR 32.75dB SSIM 0.9890</sub> |  <sub>PSNR 32.75dB SSIM 0.9890</sub> |
|    ![](Examples/bird_GT.png)     |   ![](Examples/bird_bicubic_x3.png)    |   ![](Examples/bird_srcnn_x3.png)    |
|                                  |    <sub>PSNR 32.75dB SSIM 0.9890</sub> |  <sub>PSNR 32.75dB SSIM 0.9890</sub> |
|    ![](Examples/baby_GT.png)     |   ![](Examples/baby_bicubic_x3.png)    |   ![](Examples/baby_srcnn_x3.png)    |
|                                  |    <sub>PSNR 32.75dB SSIM 0.9890</sub> |  <sub>PSNR 32.75dB SSIM 0.9890</sub> |
## Pre-requisitos

* Python 3.13
  * Numpy X.X.X
  * Torch 2.8.0
  * Torchvision X.X.X
  * Pillow X.X.X
