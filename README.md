# Hackathon Big Data 2019

Sujet 4, groupe 6. Semaine du 18 au 22 novembre 2019.

Participants :
- [Sylvain Combettes](https://www.linkedin.com/in/sylvain-combettes/), Ecole des Mines de Nancy
- [Mohammed El Yaagoubi](https://www.linkedin.com/in/melyaagoubi/), TELECOM Nancy
- [Guillaume Gatti](https://www.linkedin.com/in/guillaume-gatti-b2a482149/), TELECOM Nancy
- [Zouhair Janati-Idrissi](https://www.linkedin.com/in/zouhair-janati-idrissi/), TELECOM Nancy
- [Ali Labbaize](https://www.linkedin.com/in/alilabbaize/), TELECOM Nancy

Encadrants :
- [Adrien Coulet](https://members.loria.fr/ACoulet/), Loria
- [Joël Legrand](http://joel-legrand.fr/hugo/), Loria

Sujet : Amélioration des performances de la reconnaissances d'entités nommées biomédicales complexes (NER) avec [PGxCorpus](https://www.biorxiv.org/content/10.1101/534388v3) et [BioBERT](https://arxiv.org/abs/1901.08746).

# Running the code :

- To run the parsing code, everything is well documented in the colab version, just open it. You'll have as an output 4 tsv files for bioBERT.
- To lunch a bioBERT training or evalution you need to : 

To use BioBERT, we need pre-trained weights of BioBERT, which you can download from [NAVER GitHub repository for BioBERT pre-trained weights](https://github.com/naver/biobert-pretrained).

Run the parsing script and put the files in the biobert dir. From now on, `$NER_DIR` indicates a folder for a single dataset which should include `train_dev.tsv`, `train.tsv`, `devel.tsv` and `test.tsv`. For example, `export NER_DIR=~/bioBERT/biodatasets/NERdata/NCBI-disease`. Following command runs fine-tuining code on NER with default arguments.
```

mkdir /tmp/bioner/
python run_ner.py \
    --do_train=true \
    --do_eval=true \
    --vocab_file=$BIOBERT_DIR/vocab.txt \
    --bert_config_file=$BIOBERT_DIR/bert_config.json \
    --init_checkpoint=$BIOBERT_DIR/biobert_model.ckpt \
    --num_train_epochs=10.0 \
    --data_dir=$NER_DIR/ \
    --output_dir=/tmp/bioner/
```
You can change the arguments as you want. Once you have trained your model, you can use it in inference mode by using `--do_train=false --do_predict=true` for evaluating `test.tsv`.
The token-level evaluation result will be printed as stdout format. For example, the result for NCBI-disease dataset will be like this:

INFO:tensorflow:***** token-level evaluation results *****
INFO:tensorflow:  eval_f = 0.9028707
INFO:tensorflow:  eval_precision = 0.8839457
INFO:tensorflow:  eval_recall = 0.92273223
INFO:tensorflow:  global_step = 2571
INFO:tensorflow:  loss = 25.894125
```
