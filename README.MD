<h1> Manual de instalação </h1>

```
    python -m venv venv
```

```
.\venv\Scripts\activate
```

```
pip install -r requirements.txt
```

```
cosmic-ray new-config tutorial.toml
```
[?] Top-level module path: user.py <br>
[?] Test execution timeout (seconds): 10 <br>
[?] Test command: pytest <br>
-- MENU: Distributor -- <br>
  (0) http <br>
  (1) local <br>
[?] Enter menu selection: 1

```
    cosmic-ray init tutorial.toml tutorial.sqlite
```

```
    cr-report tutorial.sqlite --show-pending
```

```
cosmic-ray exec tutorial.toml tutorial.sqlite
```

```
cr-report tutorial.sqlite --show-pending
```