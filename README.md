# Better Call Saul

The `Better Call Saul` is inspired from a `Breaking Bad` web series character. for web development `Better Use Reflex`

![image](https://github.com/Antony-M1/better-call-saul/assets/96291963/c26b0582-698e-4f3c-9278-fa4b1e15bc8c)

# Prequisites
* Python 3.10


<details>
  <summary><h3>Local setup</h3></summary>


### Step 1: Clone the repository

```
git clone https://github.com/Antony-M1/better-call-saul.git
```

### Step 2: Create Environment
```
python3.10 -m venv .venv
```
And Activate the `Environment`, For `Linux`
```
source .venv/bin/activate
```

### Step 3: Install Requirements
```
pip install -r requirements.txt
```
</details>

<details>
    <summary><h3>Reflex User Guide</h3></summary>


### 🥳 Create your first app
Initialize the app in cuure
```
reflex init
```

### Run APP
```
reflex run
```
</details>


<details>
  <summary><h3>Debugger</h3></summary>

```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Module",
      "type": "debugpy",
      "request": "launch",
      "module": "reflex",
      "args": "run"
    },
  ]
}
```
</details>