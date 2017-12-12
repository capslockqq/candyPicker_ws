# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "candyPicker: 1 messages, 0 services")

set(MSG_I_FLAGS "-IcandyPicker:/home/ubuntu/candyPicker_ws/src/candyPicker/msg;-Istd_msgs:/opt/ros/hydro/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(candyPicker_generate_messages ALL)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(candyPicker
  "/home/ubuntu/candyPicker_ws/src/candyPicker/msg/arrayCoord.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candyPicker
)

### Generating Services

### Generating Module File
_generate_module_cpp(candyPicker
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candyPicker
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(candyPicker_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(candyPicker_generate_messages candyPicker_generate_messages_cpp)

# target for backward compatibility
add_custom_target(candyPicker_gencpp)
add_dependencies(candyPicker_gencpp candyPicker_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candyPicker_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(candyPicker
  "/home/ubuntu/candyPicker_ws/src/candyPicker/msg/arrayCoord.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candyPicker
)

### Generating Services

### Generating Module File
_generate_module_lisp(candyPicker
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candyPicker
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(candyPicker_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(candyPicker_generate_messages candyPicker_generate_messages_lisp)

# target for backward compatibility
add_custom_target(candyPicker_genlisp)
add_dependencies(candyPicker_genlisp candyPicker_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candyPicker_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(candyPicker
  "/home/ubuntu/candyPicker_ws/src/candyPicker/msg/arrayCoord.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candyPicker
)

### Generating Services

### Generating Module File
_generate_module_py(candyPicker
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candyPicker
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(candyPicker_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(candyPicker_generate_messages candyPicker_generate_messages_py)

# target for backward compatibility
add_custom_target(candyPicker_genpy)
add_dependencies(candyPicker_genpy candyPicker_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candyPicker_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candyPicker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candyPicker
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(candyPicker_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candyPicker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candyPicker
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(candyPicker_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candyPicker)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candyPicker\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candyPicker
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(candyPicker_generate_messages_py std_msgs_generate_messages_py)