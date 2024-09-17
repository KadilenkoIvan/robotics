// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ex09:srv/FullNameSumService.idl
// generated code does not contain a copyright notice

#ifndef EX09__SRV__DETAIL__FULL_NAME_SUM_SERVICE__BUILDER_HPP_
#define EX09__SRV__DETAIL__FULL_NAME_SUM_SERVICE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ex09/srv/detail/full_name_sum_service__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ex09
{

namespace srv
{

namespace builder
{

class Init_FullNameSumService_Request_first_name
{
public:
  explicit Init_FullNameSumService_Request_first_name(::ex09::srv::FullNameSumService_Request & msg)
  : msg_(msg)
  {}
  ::ex09::srv::FullNameSumService_Request first_name(::ex09::srv::FullNameSumService_Request::_first_name_type arg)
  {
    msg_.first_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ex09::srv::FullNameSumService_Request msg_;
};

class Init_FullNameSumService_Request_name
{
public:
  explicit Init_FullNameSumService_Request_name(::ex09::srv::FullNameSumService_Request & msg)
  : msg_(msg)
  {}
  Init_FullNameSumService_Request_first_name name(::ex09::srv::FullNameSumService_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_FullNameSumService_Request_first_name(msg_);
  }

private:
  ::ex09::srv::FullNameSumService_Request msg_;
};

class Init_FullNameSumService_Request_last_name
{
public:
  Init_FullNameSumService_Request_last_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FullNameSumService_Request_name last_name(::ex09::srv::FullNameSumService_Request::_last_name_type arg)
  {
    msg_.last_name = std::move(arg);
    return Init_FullNameSumService_Request_name(msg_);
  }

private:
  ::ex09::srv::FullNameSumService_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ex09::srv::FullNameSumService_Request>()
{
  return ex09::srv::builder::Init_FullNameSumService_Request_last_name();
}

}  // namespace ex09


namespace ex09
{

namespace srv
{

namespace builder
{

class Init_FullNameSumService_Response_full_name
{
public:
  Init_FullNameSumService_Response_full_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ex09::srv::FullNameSumService_Response full_name(::ex09::srv::FullNameSumService_Response::_full_name_type arg)
  {
    msg_.full_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ex09::srv::FullNameSumService_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ex09::srv::FullNameSumService_Response>()
{
  return ex09::srv::builder::Init_FullNameSumService_Response_full_name();
}

}  // namespace ex09

#endif  // EX09__SRV__DETAIL__FULL_NAME_SUM_SERVICE__BUILDER_HPP_
