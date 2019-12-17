# SeaShips
Convert SeaShips from VOC to KITTI with [vod-converter](https://github.com/umautobots/vod-converter):

```
python vod_converter/main.py --from voc --from-path ~/datasets/SeaShips --to kitti --to-path ~/datasets/SeaShips-kitti
```

When txt file is corrupt:
```
cd datasets/kitti && ls -1 training/image_2 | cut -d. -f1 > train.txt && cd -
```