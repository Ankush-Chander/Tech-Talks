#include <iostream>
#include <vector>

struct Frame { int n; };

int main() {
    std::vector<Frame> st{{1}};

    while (true) {
        auto f = st.back();

        if (f.n % 100000 == 0)
            std::cout << "depth = " << f.n << '\n';

        st.push_back({f.n + 1});
    }
}