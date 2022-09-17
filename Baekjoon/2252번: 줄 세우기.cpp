#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
vector<int> graph[32001];
vector<int> in_degree(32001, 0);
vector<bool> visited(32001, false);
queue<int> q;
void topological_sort(){
  for(int i=1; i < n+1; i++){
    if(in_degree[i] == 0){
      q.push(i);
    }
  }

  while(!(q.empty())){
    int v = q.front();
    q.pop();
    cout << v << ' ';
    for(int i: graph[v]){
      if (!visited[i]){
        in_degree[i]--;
        if(in_degree[i] == 0){
          q.push(i);
          visited[i] = true;
          }
        }
      }
    }
  }
int main() {
  cin >> n >> m;
  
  for(int i; i < m; i++){
    int a, b;
    cin >> a >> b;
    graph[a].emplace_back(b);
    in_degree[b]++;
  }
  topological_sort();
    return 0;
}#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
vector<int> graph[32001];
vector<int> in_degree(32001, 0);
vector<bool> visited(32001, false);
queue<int> q;
void topological_sort(){
  for(int i=1; i < n+1; i++){
    if(in_degree[i] == 0){
      q.push(i);
    }
  }

  while(!(q.empty())){
    int v = q.front();
    q.pop();
    cout << v << ' ';
    for(int i: graph[v]){
      if (!visited[i]){
        in_degree[i]--;
        if(in_degree[i] == 0){
          q.push(i);
          visited[i] = true;
          }
        }
      }
    }
  }
int main() {
  cin >> n >> m;
  
  for(int i; i < m; i++){
    int a, b;
    cin >> a >> b;
    graph[a].emplace_back(b);
    in_degree[b]++;
  }
  topological_sort();
    return 0;
}
