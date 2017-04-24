class VerySecureEncryption:
  def _do_once(self, message, key):
    retval = ['' for i in range(len(message))]
    for i, m in enumerate(message):
      retval[key[i]] = m
    return "".join(retval)

  def encrypt(self, message, key, K):
    for i in range(K):
      message = self._do_once(message, key)
    return message
    
if __name__ == "__main__":
  print VerySecureEncryption().encrypt("abc", [1, 2, 0], 1)
  print VerySecureEncryption().encrypt("abcde", [4, 3, 2, 1, 0], 1)
  print VerySecureEncryption().encrypt("abcde", [4, 3, 2, 1, 0], 2)
  print VerySecureEncryption().encrypt("uogcodlk", [4, 3, 6, 2, 5, 1, 0, 7], 44)