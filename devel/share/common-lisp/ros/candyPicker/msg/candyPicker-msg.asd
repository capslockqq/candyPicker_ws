
(cl:in-package :asdf)

(defsystem "candyPicker-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "arrayCoord" :depends-on ("_package_arrayCoord"))
    (:file "_package_arrayCoord" :depends-on ("_package"))
  ))