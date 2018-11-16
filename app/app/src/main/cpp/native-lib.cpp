#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_ccu_1csie_1se_hospital_1notification_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}
