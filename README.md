
# DEMAL_Model
Dual-Encoding Matching Adversarial Learning for Image Cartoonlization (TCSVT Accepted!)

<div align="center">
 <!--   <img src="images/logo.png" alt="Logo" width="47" height="30" style="margin-right: 10px;"> -->
  You can visit our paper:<a href="https://ieeexplore.ieee.org/document/10613820"> Dual-Encoding Matching Adversarial Learning for Image Cartoonlization</a>
</h1>
</div>

## Abstract
Generative Adversarial Network (GAN)-based image cartoonization has made great progress. They 
usually use a ``single-encoding adversarial feedback architecture'' to generate cartoon image in a similar cartoon-style domain. However, this architecture cannot generate a satisfactory cartoonized image with both high style similarity and visual fidelity. In this work, to relieve this problem, we propose a novel dual-encoding matching adversarial learning dubbed DEMAL for image cartoonlization. Particularly, we first design a dual-encoding matching (DEM) by using a pair of dual encoders and a statistical matching module (SM) to match the content-style feature encodings extracted separately in the statistical space. We then construct double-structure style discriminators to adversarially learn global and local feature representations of cartoon-style via the improved loss function. Furthermore, we also propose a pre-training strategy for the DEMAL to achieve the best FID and ArtFID distance. Extensive experiments have demonstrated that our proposed DEMAL achieves high visual fidelity and style similarity compared to the previous representative baseline cartoonization methods.
## Framework
![DEMAL](https://github.com/ZYDeeplearning/DEMAL_Model/blob/main/1.png)
The overall pipeline of our DEMAL framework.
## Results
![DEMAL](https://github.com/ZYDeeplearning/DEMAL_Model/blob/main/2.png)
![DEMAL](https://github.com/ZYDeeplearning/DEMAL_Model/blob/main/3.png)
![DEMAL](https://github.com/ZYDeeplearning/DEMAL_Model/blob/main/4.png)

## Environment
You can visit [Kaggle ((https://www.kaggle.com))] 
## Datasets
We use the paper's datasets (https://github.com/TachibanaYoshino/AnimeGAN). 
## Pretrained models
You can visit[Google(https://drive.google.com/drive/folders/1Bk0H3VrkdkeLuxW7Rieki-BvhqKPxNdC?usp=drive_link)], includings the training weights on the 'Hayao', 'Shinkai'', and 'Paprika'' datasets.

## Run
## Training
Inculding 20 epoch Pretraining, you can set the ``--train_init ==True``. To format training, you need run 150epoch by setting the  ``--isTrain ==True``, but 
``--train_init==False``. (Note that you need load your pretraing weight or use ours [Google(https://drive.google.com/drive/folders/1Bk0H3VrkdkeLuxW7Rieki-BvhqKPxNdC?usp=drive_link)])
## Test 
You can set the ``--isTest ==True``.
```
python main.py --xxxx.
```
## More Updating......
##  ✍️️ Citation
If you find this paper useful in your research, please consider citing:
```
@ARTICLE{10613820,
  author={Dong, Yongsheng and Zhang, Yu and Li, Xuelong},
  journal={IEEE Transactions on Circuits and Systems for Video Technology}, 
  title={Dual-Encoding Matching Adversarial Learning for Image Cartoonlization}, 
  year={2024},
  volume={34},
  number={12},
  pages={12301-12315},
  keywords={Visualization;Feature extraction;Computer architecture;Task analysis;Image color analysis;Generative adversarial networks;Training;Cartoonization;dual-encoding matching;style similarity;high visual fidelity},
  doi={10.1109/TCSVT.2024.3416315}}
