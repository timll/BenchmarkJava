import zipfile
import glob
import os

WAR_PATH = "target/benchmark.war"
PREPREND = "target/benchmark/"
TEST_CODE = "WEB-INF/classes/org/owasp/benchmark/testcode"
ALWAYS_KEEP = [
    "WEB-INF/classes/org/owasp/benchmark/helpers",
    "WEB-INF/classes/org/owasp/benchmark/service",
]

for f in glob.glob(f"{PREPREND}/{TEST_CODE}/*.class"):
    path, name = f.rsplit("/", 1)
    if "$" in name:
        continue
    testcase = name.replace(".class", "")
    zippath = path.replace(PREPREND, "")
    with zipfile.ZipFile(f"target/splitted/{testcase}.war", mode='w') as arc:
        for keep in ALWAYS_KEEP:
            for dirpath, _, files in os.walk(f"{PREPREND}/{keep}"):
                for file in files:
                    arc.write(os.path.join(dirpath, file), os.path.join(keep, file))

        arc.write(f, os.path.join(zippath, name))
        for innerClass in glob.glob(f"{PREPREND}/{TEST_CODE}/{testcase}$*.class"):
            arc.write(innerClass, innerClass.replace(PREPREND, ""))