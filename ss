[1mdiff --git a/.gitignore b/.gitignore[m
[1mindex 7b97468..4b0556e 100644[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@ -1,11 +1,33 @@[m
[31m-# Python-generated files[m
[32m+[m[32m# Python[m
 __pycache__/[m
[31m-*.py[oc][m
[32m+[m[32m*.py[cod][m
[32m+[m[32m*.pyo[m
[32m+[m[32m*.pyd[m
[32m+[m
[32m+[m[32m# Virtual environments[m
[32m+[m[32m.venv/[m
[32m+[m[32mvenv/[m
[32m+[m[32menv/[m
[32m+[m
[32m+[m[32m# Build / packaging[m
 build/[m
 dist/[m
[32m+[m[32m*.egg-info/[m
 wheels/[m
[31m-*.egg-info[m
 [m
[31m-# Virtual environments[m
[31m-.venv[m
[31m-venv/[m
[32m+[m[32m# Environment / secrets[m
[32m+[m[32m.env[m
[32m+[m[32m.env.*[m
[32m+[m
[32m+[m[32m# IDE[m
[32m+[m[32m.idea/[m
[32m+[m[32m.vscode/[m
[32m+[m
[32m+[m[32m# Test / coverage[m
[32m+[m[32m.pytest_cache/[m
[32m+[m[32m.coverage[m
[32m+[m[32mhtmlcov/[m
[32m+[m
[32m+[m[32m# OS files[m
[32m+[m[32m.DS_Store[m
[32m+[m[32mThumbs.db[m
\ No newline at end of file[m
