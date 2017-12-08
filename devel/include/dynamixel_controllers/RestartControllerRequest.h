/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/ubuntu/candyPicker_ws/src/dynamixel_motor/dynamixel_controllers/srv/RestartController.srv
 *
 */


#ifndef DYNAMIXEL_CONTROLLERS_MESSAGE_RESTARTCONTROLLERREQUEST_H
#define DYNAMIXEL_CONTROLLERS_MESSAGE_RESTARTCONTROLLERREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dynamixel_controllers
{
template <class ContainerAllocator>
struct RestartControllerRequest_
{
  typedef RestartControllerRequest_<ContainerAllocator> Type;

  RestartControllerRequest_()
    : port_name()
    , package_path()
    , module_name()
    , class_name()
    , controller_name()
    , dependencies()  {
    }
  RestartControllerRequest_(const ContainerAllocator& _alloc)
    : port_name(_alloc)
    , package_path(_alloc)
    , module_name(_alloc)
    , class_name(_alloc)
    , controller_name(_alloc)
    , dependencies(_alloc)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _port_name_type;
  _port_name_type port_name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _package_path_type;
  _package_path_type package_path;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _module_name_type;
  _module_name_type module_name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _class_name_type;
  _class_name_type class_name;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _controller_name_type;
  _controller_name_type controller_name;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _dependencies_type;
  _dependencies_type dependencies;




  typedef boost::shared_ptr< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct RestartControllerRequest_

typedef ::dynamixel_controllers::RestartControllerRequest_<std::allocator<void> > RestartControllerRequest;

typedef boost::shared_ptr< ::dynamixel_controllers::RestartControllerRequest > RestartControllerRequestPtr;
typedef boost::shared_ptr< ::dynamixel_controllers::RestartControllerRequest const> RestartControllerRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace dynamixel_controllers

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7785d708c83a180befd2fe3450dd9d41";
  }

  static const char* value(const ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7785d708c83a180bULL;
  static const uint64_t static_value2 = 0xefd2fe3450dd9d41ULL;
};

template<class ContainerAllocator>
struct DataType< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dynamixel_controllers/RestartControllerRequest";
  }

  static const char* value(const ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string port_name\n\
string package_path\n\
string module_name\n\
string class_name\n\
string controller_name\n\
string[] dependencies\n\
";
  }

  static const char* value(const ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.port_name);
      stream.next(m.package_path);
      stream.next(m.module_name);
      stream.next(m.class_name);
      stream.next(m.controller_name);
      stream.next(m.dependencies);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct RestartControllerRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dynamixel_controllers::RestartControllerRequest_<ContainerAllocator>& v)
  {
    s << indent << "port_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.port_name);
    s << indent << "package_path: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.package_path);
    s << indent << "module_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.module_name);
    s << indent << "class_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.class_name);
    s << indent << "controller_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.controller_name);
    s << indent << "dependencies[]" << std::endl;
    for (size_t i = 0; i < v.dependencies.size(); ++i)
    {
      s << indent << "  dependencies[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.dependencies[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // DYNAMIXEL_CONTROLLERS_MESSAGE_RESTARTCONTROLLERREQUEST_H
