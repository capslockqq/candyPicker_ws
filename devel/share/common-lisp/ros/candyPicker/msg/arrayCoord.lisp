; Auto-generated. Do not edit!


(cl:in-package candyPicker-msg)


;//! \htmlinclude arrayCoord.msg.html

(cl:defclass <arrayCoord> (roslisp-msg-protocol:ros-message)
  ((arrayCoord
    :reader arrayCoord
    :initarg :arrayCoord
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass arrayCoord (<arrayCoord>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <arrayCoord>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'arrayCoord)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name candyPicker-msg:<arrayCoord> is deprecated: use candyPicker-msg:arrayCoord instead.")))

(cl:ensure-generic-function 'arrayCoord-val :lambda-list '(m))
(cl:defmethod arrayCoord-val ((m <arrayCoord>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader candyPicker-msg:arrayCoord-val is deprecated.  Use candyPicker-msg:arrayCoord instead.")
  (arrayCoord m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <arrayCoord>) ostream)
  "Serializes a message object of type '<arrayCoord>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'arrayCoord))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'arrayCoord))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <arrayCoord>) istream)
  "Deserializes a message object of type '<arrayCoord>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'arrayCoord) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'arrayCoord)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<arrayCoord>)))
  "Returns string type for a message object of type '<arrayCoord>"
  "candyPicker/arrayCoord")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'arrayCoord)))
  "Returns string type for a message object of type 'arrayCoord"
  "candyPicker/arrayCoord")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<arrayCoord>)))
  "Returns md5sum for a message object of type '<arrayCoord>"
  "aa2f1e5568cfd30f3f7a43cd3c032633")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'arrayCoord)))
  "Returns md5sum for a message object of type 'arrayCoord"
  "aa2f1e5568cfd30f3f7a43cd3c032633")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<arrayCoord>)))
  "Returns full string definition for message of type '<arrayCoord>"
  (cl:format cl:nil "int32[] arrayCoord~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'arrayCoord)))
  "Returns full string definition for message of type 'arrayCoord"
  (cl:format cl:nil "int32[] arrayCoord~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <arrayCoord>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'arrayCoord) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <arrayCoord>))
  "Converts a ROS message object to a list"
  (cl:list 'arrayCoord
    (cl:cons ':arrayCoord (arrayCoord msg))
))
