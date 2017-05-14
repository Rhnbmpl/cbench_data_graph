# cbench_data_graph
Plot the data from the cbench controller benchmark tool. Can plot from multiple files to compare the results.Works on linux and Windows with python 3 installed.

Dependencies: matplotlib (installation: pip3 install matplotlib)

First make it executable(for linux users): sudo chmod +x cbench_data.py

Enter the file path(relative to where cbench_data.py is stored) as arguments:(Linux) ./cbench_data.py file1.txt file2.txt file3.txt....

(Windows): python3 cbench_data.py file1.txt file2.txt file3.txt....

For changing the names on the Legend,X/Y-Axis,Heading do it manually in the cbench_data.py. Places to change are marked.
Further improvements will come up.
