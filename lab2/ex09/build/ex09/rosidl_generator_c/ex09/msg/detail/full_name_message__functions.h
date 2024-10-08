// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from ex09:msg/FullNameMessage.idl
// generated code does not contain a copyright notice

#ifndef EX09__MSG__DETAIL__FULL_NAME_MESSAGE__FUNCTIONS_H_
#define EX09__MSG__DETAIL__FULL_NAME_MESSAGE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "ex09/msg/rosidl_generator_c__visibility_control.h"

#include "ex09/msg/detail/full_name_message__struct.h"

/// Initialize msg/FullNameMessage message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * ex09__msg__FullNameMessage
 * )) before or use
 * ex09__msg__FullNameMessage__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
bool
ex09__msg__FullNameMessage__init(ex09__msg__FullNameMessage * msg);

/// Finalize msg/FullNameMessage message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
void
ex09__msg__FullNameMessage__fini(ex09__msg__FullNameMessage * msg);

/// Create msg/FullNameMessage message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * ex09__msg__FullNameMessage__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
ex09__msg__FullNameMessage *
ex09__msg__FullNameMessage__create();

/// Destroy msg/FullNameMessage message.
/**
 * It calls
 * ex09__msg__FullNameMessage__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
void
ex09__msg__FullNameMessage__destroy(ex09__msg__FullNameMessage * msg);

/// Check for msg/FullNameMessage message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
bool
ex09__msg__FullNameMessage__are_equal(const ex09__msg__FullNameMessage * lhs, const ex09__msg__FullNameMessage * rhs);

/// Copy a msg/FullNameMessage message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
bool
ex09__msg__FullNameMessage__copy(
  const ex09__msg__FullNameMessage * input,
  ex09__msg__FullNameMessage * output);

/// Initialize array of msg/FullNameMessage messages.
/**
 * It allocates the memory for the number of elements and calls
 * ex09__msg__FullNameMessage__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
bool
ex09__msg__FullNameMessage__Sequence__init(ex09__msg__FullNameMessage__Sequence * array, size_t size);

/// Finalize array of msg/FullNameMessage messages.
/**
 * It calls
 * ex09__msg__FullNameMessage__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
void
ex09__msg__FullNameMessage__Sequence__fini(ex09__msg__FullNameMessage__Sequence * array);

/// Create array of msg/FullNameMessage messages.
/**
 * It allocates the memory for the array and calls
 * ex09__msg__FullNameMessage__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
ex09__msg__FullNameMessage__Sequence *
ex09__msg__FullNameMessage__Sequence__create(size_t size);

/// Destroy array of msg/FullNameMessage messages.
/**
 * It calls
 * ex09__msg__FullNameMessage__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
void
ex09__msg__FullNameMessage__Sequence__destroy(ex09__msg__FullNameMessage__Sequence * array);

/// Check for msg/FullNameMessage message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
bool
ex09__msg__FullNameMessage__Sequence__are_equal(const ex09__msg__FullNameMessage__Sequence * lhs, const ex09__msg__FullNameMessage__Sequence * rhs);

/// Copy an array of msg/FullNameMessage messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_ex09
bool
ex09__msg__FullNameMessage__Sequence__copy(
  const ex09__msg__FullNameMessage__Sequence * input,
  ex09__msg__FullNameMessage__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // EX09__MSG__DETAIL__FULL_NAME_MESSAGE__FUNCTIONS_H_
