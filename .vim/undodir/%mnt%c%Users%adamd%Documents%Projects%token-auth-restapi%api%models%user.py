Vim�UnDo� b�X�kMk�\�q�ݯf9wX��w���V~8                                       _�>�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _�;     �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�<�     �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�=     �   
                      self.password = 5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             _�=     �   
              0        self.password = generate_password_hash()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�=     �   
              8        self.password = generate_password_hash(password)5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             _�=$     �   
              8        self.password = generate_password_hash(password)5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             _�=<     �                     �               5�_�   	              
      #    ����                                                                                                                                                                                                                                                                                                                                                             _�=\     �                 $        return check_password_hash()5�_�   
                    *    ����                                                                                                                                                                                                                                                                                                                                                             _�=a     �                 +        return check_password_hash(pwhash,)5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             _�=k    �                 -        return check_password_hash(password,)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�=~     �   
            ?        return self.password = generate_password_hash(password)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�=�     �   
            ?        return self.password = generate_password_hash(password)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�=�    �   
            <        retuself.password = generate_password_hash(password)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�=�    �                 �               �                  Ifrom werkzeug.security import generate_password_hash, check_password_hash    from database.database import db       class User(db.Model):       __tablename__ = 'users'   0    id = db.Column(db.Integer, primary_key=True)   3    username = db.Column(db.String(32), index=True)   '    password = db.Column(db.String(64))       &    def hash_password(self, password):   8        self.password = generate_password_hash(password)       (    def verify_password(self, password):   ;        return check_password_hash(password, self.password)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�=�     �                     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�>|     �                     �               5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             _�>�    �                   �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�<�     �                 5��