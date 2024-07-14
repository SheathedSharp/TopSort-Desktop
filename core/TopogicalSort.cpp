#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

struct Course {
    string name;  // 课程名
    vector<Course*> prerequisites;  // 对应的先修课程的指针向量
    int indegree;  // 入度（有多少个先修条件）
    bool visited;  // 判断课程是否被访问过
    Course(const string& n) : name(n), indegree(0), visited(false) {}  // 构造函数
};

vector<vector<string>> allTopologicalSorts;

void dfs(vector<Course*>& courses, vector<string>& result) {
    if (result.size() == courses.size()) {
        allTopologicalSorts.push_back(result);
        return; // 递归终止条件：完成了一次拓扑排序
    }

    for (size_t i = 0; i < courses.size(); ++i) { // 遍历每个课程
        Course* course = courses[i]; // 当前课程

        if (course->indegree == 0 && !course->visited) { // 如果当前课程的入度为0且未被访问过
            course->visited = true; // 标记当前课程已访问

            result.push_back(course->name); // 将当前课程添加到当前排列中

            for (size_t j = 0; j < course->prerequisites.size(); ++j) { // 减少当前课程的邻接课程的入度
                Course* prerequisite = course->prerequisites[j];
                prerequisite->indegree--;
            }

            dfs(courses, result);       //递归

            course->visited = false; // 标记当前课程为未访问状态
            for (size_t j = 0; j < course->prerequisites.size(); ++j) { // 回溯：撤销之前的修改
                Course* prerequisite = course->prerequisites[j];
                prerequisite->indegree++; // 恢复后续邻接课程的入度
            }
            result.pop_back(); // 移除当前排列中的最后一门课程
        }
    }
}

bool printAllTopologicalSorts(vector<Course*>& courses) {
    vector<string> result;
    dfs(courses, result);
    return !allTopologicalSorts.empty();
}

void shuchu(vector<Course*>& courses) {
    int count = 0;
    for (size_t i = 0; i < allTopologicalSorts.size(); ++i) {
        cout << "sort ruselt_" << ++count << ':';
        for (size_t j = 0; j < allTopologicalSorts[i].size(); ++j) {
            cout << allTopologicalSorts[i][j] << " ";
        }
        cout << endl;
        if (i != allTopologicalSorts.size() - 1) {
            cout << "---------------------" << endl;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <filename>" << endl;
        return 0;
    }

    string filename = argv[1];  
    vector<Course*> courses;
    unordered_map<string, Course*> courseMap;

    ifstream file(filename);
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            if (line.empty()) {
                continue;
            }

            line = line.substr(1, line.size() - 2);
            stringstream ss(line);
            string courseName, prereqName;
            getline(ss, courseName, ',');
            getline(ss, prereqName);

            Course* course = courseMap[courseName];
            if (!course) {
                course = new Course(courseName);
                courses.push_back(course);
                courseMap[courseName] = course;
            }

            Course* prereq = courseMap[prereqName];
            if (!prereq) {
                prereq = new Course(prereqName);
                courses.push_back(prereq);
                courseMap[prereqName] = prereq;
            }

            course->prerequisites.push_back(prereq);
            prereq->indegree++;
        }
        file.close();
    } else {
        cout << "无法打开文件" << endl;
        return 0;
    }

    if (printAllTopologicalSorts(courses)) {
        shuchu(courses);
    } else {
        cout << "存在循环依赖关系" << endl;
    }

    for (size_t i = 0; i < courses.size(); i++) {
        delete courses[i];
    }
    courses.clear();

    return 0;
}

