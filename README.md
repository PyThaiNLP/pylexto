# PyLexTo

LexTo with Python 2 & 3 Wrapper 

Fork by https://github.com/Remixman/PythonLexTo

## Install

Make sure CLASSPATH and JAVA_HOME are set and

```
pip install https://github.com/wannaphongcom/pylexto/archive/master.zip
```

## Using

```python
from pylexto import LexTo
lexto = LexTo()
text = u"แมวกินปลาแมวมันชอบนอนนอนกลางวันนอนแล้วนอนอีกเป็นสัตว์ที่ขี้เกียจจริงๆเลยแมวแต่แมวมันเข้ากับคนได้ดีฉันชอบแมว"
words, types = lexto.tokenize(text)
print('|'.join(words))
print(types)
```

## License

### PyLexTo

MIT License

Copyright (c) 2017 Wannaphong Phatthiyaphaibun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### LexTo

```
/**
 * Licensed under the CC-GNU Lesser General Public License, Version 2.1 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://creativecommons.org/licenses/LGPL/2.1/
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

```