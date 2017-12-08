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
 * Auto-generated by gensrv_cpp from file /home/ubuntu/candyPicker_ws/src/dynamixel_motor/dynamixel_controllers/srv/SetComplianceSlope.srv
 *
 */


#ifndef DYNAMIXEL_CONTROLLERS_MESSAGE_SETCOMPLIANCESLOPE_H
#define DYNAMIXEL_CONTROLLERS_MESSAGE_SETCOMPLIANCESLOPE_H

#include <ros/service_traits.h>


#include <dynamixel_controllers/SetComplianceSlopeRequest.h>
#include <dynamixel_controllers/SetComplianceSlopeResponse.h>


namespace dynamixel_controllers
{

struct SetComplianceSlope
{

typedef SetComplianceSlopeRequest Request;
typedef SetComplianceSlopeResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetComplianceSlope
} // namespace dynamixel_controllers


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::dynamixel_controllers::SetComplianceSlope > {
  static const char* value()
  {
    return "0b655cbe1b74daf357824dcc427c1004";
  }

  static const char* value(const ::dynamixel_controllers::SetComplianceSlope&) { return value(); }
};

template<>
struct DataType< ::dynamixel_controllers::SetComplianceSlope > {
  static const char* value()
  {
    return "dynamixel_controllers/SetComplianceSlope";
  }

  static const char* value(const ::dynamixel_controllers::SetComplianceSlope&) { return value(); }
};


// service_traits::MD5Sum< ::dynamixel_controllers::SetComplianceSlopeRequest> should match 
// service_traits::MD5Sum< ::dynamixel_controllers::SetComplianceSlope > 
template<>
struct MD5Sum< ::dynamixel_controllers::SetComplianceSlopeRequest>
{
  static const char* value()
  {
    return MD5Sum< ::dynamixel_controllers::SetComplianceSlope >::value();
  }
  static const char* value(const ::dynamixel_controllers::SetComplianceSlopeRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::dynamixel_controllers::SetComplianceSlopeRequest> should match 
// service_traits::DataType< ::dynamixel_controllers::SetComplianceSlope > 
template<>
struct DataType< ::dynamixel_controllers::SetComplianceSlopeRequest>
{
  static const char* value()
  {
    return DataType< ::dynamixel_controllers::SetComplianceSlope >::value();
  }
  static const char* value(const ::dynamixel_controllers::SetComplianceSlopeRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::dynamixel_controllers::SetComplianceSlopeResponse> should match 
// service_traits::MD5Sum< ::dynamixel_controllers::SetComplianceSlope > 
template<>
struct MD5Sum< ::dynamixel_controllers::SetComplianceSlopeResponse>
{
  static const char* value()
  {
    return MD5Sum< ::dynamixel_controllers::SetComplianceSlope >::value();
  }
  static const char* value(const ::dynamixel_controllers::SetComplianceSlopeResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::dynamixel_controllers::SetComplianceSlopeResponse> should match 
// service_traits::DataType< ::dynamixel_controllers::SetComplianceSlope > 
template<>
struct DataType< ::dynamixel_controllers::SetComplianceSlopeResponse>
{
  static const char* value()
  {
    return DataType< ::dynamixel_controllers::SetComplianceSlope >::value();
  }
  static const char* value(const ::dynamixel_controllers::SetComplianceSlopeResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DYNAMIXEL_CONTROLLERS_MESSAGE_SETCOMPLIANCESLOPE_H
