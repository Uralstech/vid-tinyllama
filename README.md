# Vid TinyLLaMA
Run TinyLLaMA on your PC.

## TinyLLaMA
Go to ***<https://huggingface.co/PY007/TinyLlama-1.1B-Chat-v0.2>*** to download TinyLLaMA or check out ***<https://github.com/jzhang38/TinyLlama>*** for more info.

## Notes
* You can reduce the max tokens and length of the answer (`src/main.py`, line **25** and **26**) to make the model run faster.

## Docker
If you do not want to use docker to run the model, you can just run:

#### Bash
```bash
pip3 install -r requirements.txt
python3 src/main.py
```

#### CMD (Windows)
```cmd
pip install -r requirements.txt
python src/main.py
```

## License
The license and notice for the code in the repository can be found here: (https://github.com/Uralstech/Vid-TinyLLaMA/blob/main/LICENSE) and here: (https://github.com/Uralstech/Vid-TinyLLaMA/blob/main/NOTICE) respectively.