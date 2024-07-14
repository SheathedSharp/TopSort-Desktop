# Desktop-portable-topological-sorting-application

## Running Environment
- **OS**: Mac
- **IDE**: VSCode
- **Interpreter**: Python v3.9
- **External Libraries**: PySide2 v5.15.2.1, networkx v2.5.1, matplotlib v3.3.4
- **GUI Tool**: QtDesigner

## Project Structure

```commandline
TopologicalSort_app
├─build(packaged software)
├─core (core algorithms)
├─data (imported file information)
├─dist (different versions of the released software)
├─docs (all documentation)
├─statics (static resources)
```

## Quick Deployment
- First, create a virtual environment by entering the command `mamba create -n TSA python=3.9` to create a virtual environment named TSA.
- Activate the newly created virtual environment by entering the command `conda activate TSA`.
- Install external dependencies by entering the command `mamba install --file requirements.txt`.

## User Guide
- Using the previously created environment, run the main file with the command `python main.py`.

[![Launch Application](https://pic.imgdb.cn/item/66936984d9c307b7e95ee99d.png)](https://github.com/hiddenSharp429/Desktop-portable-topological-sorting-application)

- Select the file to import, or manually input data in a specified format to add.

[![Import Data](https://pic.imgdb.cn/item/66936987d9c307b7e95eed68.png)](https://github.com/hiddenSharp429/Desktop-portable-topological-sorting-application)

- After completing the data input, click the `generate` button to perform the topological sorting.

[![Generate Topological Sort](https://pic.imgdb.cn/item/66936987d9c307b7e95eede8.png)](https://github.com/hiddenSharp429/Desktop-portable-topological-sorting-application)

- The bottom left will display the result of the topological sort, and the right side will show the topological graph.
- You can choose to export the topological result (.txt) or the topological graph (.png).

[![Topological Sort Result](https://pic.imgdb.cn/item/66936989d9c307b7e95eefdf.png)](https://github.com/hiddenSharp429/Desktop-portable-topological-sorting-application)

[![Topological Graph](https://pic.imgdb.cn/item/66936989d9c307b7e95ef050.png)](https://github.com/hiddenSharp429/Desktop-portable-topological-sorting-application)