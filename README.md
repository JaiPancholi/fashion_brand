# Image Classification on Fashion Sites
## Project Plan
1. First collect a lot of image data across many different fashion sites

2. Label the images by clustering the same person aross a brand so that we can say uniqilo-a for all images of a single model featured on uniqlo, uniqlo-b for another person etc. Some unsupervised approach is needed.

3. Find Eigenfaces across the dataset - attempt to show the distinction between brands and who they cast

4. Build a predictor method to take in a new picture and classify them into a brand.



# Clone Forked Facenet Repo



git clone https://github.com/davidsandberg/facenet.git

python facenet/src/align/align_dataset_mtcnn.py data/images/raw_test/ data/images/processed_facenet/

python facenet/src/compare.py models/20180402-114759/ data/images/raw/tom_ford_male_69 data/images/raw/tom_ford_male_70 data/images/raw/tom_ford_male_71 data/images/raw/tom_ford_male_72 data/images/raw/tom_ford_male_73 data/images/raw/tom_ford_male_74 --image_size 160 --margin 32 --gpu_memory_fraction 0

python facenet/src/export_embeddings.py models/20180402-114759/ data/images/processed_facenet/ 

### Adding Submodules
```bash
# first time only 
git submodule update --init --recursive

# any further time
git submodule add https://github.com/JaiPancholi/facenet.git facenet
```
<!-- 
```bash
git clone --recurse-submodules REPOSITORY
``` -->

To pull changes on updates to submodules you can use
```bash
git submodule update --recursive --remote
```


### Removing Submodules
To remove a submodule you need to:

- Delete the relevant section from the .gitmodules file.
- Stage the .gitmodules changes git add .gitmodules
- Delete the relevant section from .git/config.
- Run git rm --cached path_to_submodule (no trailing slash).
- Run rm -rf .git/modules/path_to_submodule (no trailing slash).
- Commit git commit -m "Removed submodule <name>"
- Delete the now untracked submodule files rm -rf path_to_submodule
