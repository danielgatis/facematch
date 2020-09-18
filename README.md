
# Facematch

[![Downloads](https://pepy.tech/badge/facematch)](https://pepy.tech/project/facematch)
[![Downloads](https://pepy.tech/badge/facematch/month)](https://pepy.tech/project/facematch/month)
[![Downloads](https://pepy.tech/badge/facematch/week)](https://pepy.tech/project/facematch/week)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://img.shields.io/badge/License-MIT-blue.svg)

Facematch is a tool to verifies if two photos contain the same person.

<table>
    <thead>
        <tr>
            <td>input1</td>
            <td>input2</td>
            <td>output</td>
            <td>result</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel1.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/doc.png" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel1-doc.png" width="100" /></td>
            <td><span>{"match": true, "distance": 0.38913072553055295}</span></td>
        </tr>
        <tr>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel2.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/doc.png" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel2-doc.png" width="100" /></td>
            <td><span>{"match": true, "distance": 0.5131670729305189}</span></td>
        </tr>
        <tr>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel1.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel2.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel1-daniel2.png" width="100" /></td>
            <td><span>{"match": true, "distance": 0.4370069082351905}</span></td>
        </tr>
        <tr>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/ronaldinho1.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/doc.png" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/ronaldinho1-doc.png" width="100" /></td>
            <td><span>{"match": false, "distance": 0.7838337220196059}</span></td>
        </tr>
        <tr>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel1.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/ronaldinho1.jpg" width="100" /></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/facematch/master/examples/daniel1-ronaldinho1.png" width="100" /></td>
            <td><span>{"match": false, "distance": 0.8705370438394476}</span></td>
        </tr>
    </tbody>
</table>

### Installation

Install it from pypi

```bash
    pip install facematch
```

### Usage as a cli

Without output image
```bash
    facematch input1.png input2.png
```

With output image
```bash
    facematch -o output.png input1.png input2.png
```

### Usage as a library

In `app.py`

```python
    from facematch.face import match

    f = open('img1.png', 'rb')
    data1 = f.read()
    f.close()

    f = open('img2.png', 'rb')
    data2 = f.read()
    f.close()

    result, distance, data = match(data1, data2)

    f = open('out.png', 'wb')
    f.write(data)
    f.close()

    print(distance)
    print(result)
```

Then run
```
    python app.py
```

### License

Copyright (c) 2020-present [Daniel Gatis](https://github.com/danielgatis)

Licensed under [MIT License](./LICENSE.txt)
